import esphome.codegen as cg
from esphome.components import switch, web_server
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
    ICON_BLUETOOTH,
    ICON_PULSE,
    CONF_ID,
)

from .. import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA, m5stack_pps_ns, M5StackPPSComponent

OutputEnableSwitch = m5stack_pps_ns.class_("OutputEnableSwitch", cg.Component, switch.Switch)

CONF_OUTPUT_ENABLE = "output_enable"

CONFIG_SCHEMA = cv.All(
    switch.switch_schema(OutputEnableSwitch, default_restore_mode="DISABLED")
      .extend(cv.COMPONENT_SCHEMA)
      .extend({
        cv.Required(CONF_M5STACK_PPS_ID): cv.use_id(M5StackPPSComponent),
      })
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await switch.register_switch(var, config)
    paren = await cg.get_variable(config[CONF_M5STACK_PPS_ID])
    cg.add(var.set_parent(paren))
    cg.add(paren.set_output_enable_switch(var))
