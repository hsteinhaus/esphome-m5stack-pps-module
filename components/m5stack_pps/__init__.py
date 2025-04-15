import esphome.codegen as cg
from esphome.components import i2c
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]

CODEOWNERS = ["@hsteinhaus"]

m5stack_pps_ns = cg.esphome_ns.namespace("m5stack_pps")
M5StackPPSComponent = m5stack_pps_ns.class_("M5StackPPSComponent", cg.Component)

CONF_M5STACK_PPS_ID = "m5stack_pps"

M5STACK_PPS_COMPONENT_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_M5STACK_PPS_ID): cv.use_id(M5StackPPSComponent),
    }
)

CONFIG_SCHEMA = cv.All(
    cv.Schema({cv.GenerateID(): cv.declare_id(M5StackPPSComponent)})
    .extend(cv.polling_component_schema("1s"))
    .extend(i2c.i2c_device_schema(0x35))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)