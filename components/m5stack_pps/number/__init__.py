import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import number, i2c
from esphome.const import CONF_ID, CONF_MODE, CONF_VOLTAGE, CONF_CURRENT, DEVICE_CLASS_VOLTAGE, DEVICE_CLASS_CURRENT, ENTITY_CATEGORY_CONFIG

from .. import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA, m5stack_pps_ns, M5StackPPSComponent

DEPENDENCIES = ["i2c"]

OutputVoltageNumber = m5stack_pps_ns.class_("OutputVoltageNumber", number.Number)
OutputCurrentNumber = m5stack_pps_ns.class_("OutputCurrentNumber", number.Number)

CONFIG_SCHEMA = M5STACK_PPS_COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_M5STACK_PPS_ID): cv.use_id(M5StackPPSComponent),
        cv.Optional(CONF_VOLTAGE): number.number_schema(
            OutputVoltageNumber,
            device_class=DEVICE_CLASS_VOLTAGE,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon="mdi:arrow-collapse-up"
        ),
        cv.Optional(CONF_CURRENT): number.number_schema(
            OutputCurrentNumber,
            device_class=DEVICE_CLASS_CURRENT,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon="mdi:dc-current"
        ),
    }
)



async def to_code(config):
    m5stack_pps_component = await cg.get_variable(config[CONF_M5STACK_PPS_ID])

    if voltage_config := config.get(CONF_VOLTAGE):
        n = await number.new_number(
            voltage_config, min_value=0.5, max_value=30, step=0.1
        )
        await cg.register_parented(n, config[CONF_M5STACK_PPS_ID])
        cg.add(m5stack_pps_component.set_output_voltage_number(n))

    if current_config := config.get(CONF_CURRENT):
        n = await number.new_number(
            current_config, min_value=0, max_value=5, step=0.1
        )
        await cg.register_parented(n, config[CONF_M5STACK_PPS_ID])
        cg.add(m5stack_pps_component.set_output_current_number(n))
