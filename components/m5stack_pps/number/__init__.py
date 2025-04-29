import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import number, web_server
from esphome.const import CONF_ID, CONF_STEP, CONF_CHANNEL, CONF_VOLTAGE, CONF_CURRENT, DEVICE_CLASS_VOLTAGE, DEVICE_CLASS_CURRENT, ENTITY_CATEGORY_CONFIG

from .. import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA, m5stack_pps_ns, M5StackPPSComponent

DEPENDENCIES = ["i2c"]

OutputNumber = m5stack_pps_ns.class_("OutputNumber", cg.Component, number.Number)
OutputChannel = m5stack_pps_ns.enum("OutputChannel")


OUTPUT_CHANNELS = {
    CONF_VOLTAGE: OutputChannel.OUTPUT_VOLTAGE,
    CONF_CURRENT: OutputChannel.OUTPUT_CURRENT,
}


CONFIG_SCHEMA = cv.All(
    number.number_schema(OutputNumber)
      .extend(cv.COMPONENT_SCHEMA)
      .extend({
        cv.Required(CONF_M5STACK_PPS_ID): cv.use_id(M5StackPPSComponent),
        cv.Required(CONF_CHANNEL): cv.enum(OUTPUT_CHANNELS),
        cv.Optional(CONF_STEP): cv.float_,
      })
)


async def to_code(config):
    output_channel = config[CONF_CHANNEL]
    var = cg.new_Pvariable(config[CONF_ID], OUTPUT_CHANNELS[output_channel])
    await cg.register_component(var, config)
    paren = await cg.get_variable(config[CONF_M5STACK_PPS_ID])

    step_config = config.get(CONF_STEP)

    if output_channel == CONF_VOLTAGE:
        await number.register_number(var, config, min_value=0.5, max_value=30, step=step_config or 0.1)
        cg.add(var.set_parent(paren))
        cg.add(paren.set_output_voltage_number(var))
    else:
        await number.register_number(var, config, min_value=0, max_value=5, step=step_config or 0.001)
        cg.add(var.set_parent(paren))
        cg.add(paren.set_output_current_number(var))


