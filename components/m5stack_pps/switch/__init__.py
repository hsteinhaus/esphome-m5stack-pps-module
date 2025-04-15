import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
    ICON_BLUETOOTH,
    ICON_PULSE,
)

from .. import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA, m5stack_pps_ns, M5StackPPSComponent

OutputEnableSwitch = m5stack_pps_ns.class_("OutputEnableSwitch", switch.Switch)

CONF_OUTPUT_ENABLE = "output_enable"

CONFIG_SCHEMA = M5STACK_PPS_COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_M5STACK_PPS_ID): cv.use_id(M5StackPPSComponent),
        cv.Optional(CONF_OUTPUT_ENABLE): switch.switch_schema(
            OutputEnableSwitch,
            device_class=DEVICE_CLASS_SWITCH,
            entity_category=ENTITY_CATEGORY_CONFIG,
            icon=ICON_PULSE,
        ),
    }
)

async def to_code(config):
    m5stack_pps_component = await cg.get_variable(config[CONF_M5STACK_PPS_ID])

    if mode_config := config.get(CONF_OUTPUT_ENABLE):
        s = await switch.new_switch(mode_config)
        await cg.register_parented(s, config[CONF_M5STACK_PPS_ID])
        cg.add(m5stack_pps_component.set_output_enable_switch(s))
