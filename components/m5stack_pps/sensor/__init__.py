import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor
from esphome.const import (
    CONF_ID,
    CONF_MODE,
    CONF_CHANNEL,
    CONF_CURRENT,
    CONF_VOLTAGE,
    CONF_POWER,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_WATT,
)

from .. import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA, m5stack_pps_ns, M5StackPPSComponent

DEPENDENCIES = ["i2c"]

TYPES = {
    CONF_MODE: sensor.sensor_schema(
        accuracy_decimals=0,
    ),
    CONF_CURRENT: sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_CURRENT,
    ),
    CONF_VOLTAGE: sensor.sensor_schema(
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_POWER: sensor.sensor_schema(
        unit_of_measurement=UNIT_WATT,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_POWER,
    ),
}

InputSensor = m5stack_pps_ns.class_("InputSensor", cg.Component, sensor.Sensor)
SensorChannel = m5stack_pps_ns.enum("OutputChannel")

SENSOR_CHANNELS = {
    CONF_MODE: SensorChannel.POWER,
    CONF_VOLTAGE: SensorChannel.VOLTAGE,
    CONF_CURRENT: SensorChannel.CURRENT,
    CONF_POWER: SensorChannel.POWER,
}

CONFIG_SCHEMA = M5STACK_PPS_COMPONENT_SCHEMA.extend(
    {cv.GenerateID(): cv.declare_id(InputSensor)}
).extend({cv.Optional(channel): schema for channel, schema in TYPES.items()})



async def to_code(config):
    paren = await cg.get_variable(config[CONF_M5STACK_PPS_ID])
    var = cg.new_Pvariable(config[CONF_ID])

    for channel in TYPES:
        if channel_config := config.get(channel):
            sens = await sensor.new_sensor(channel_config)
            cg.add(getattr(paren, f"set_{channel}_sensor")(sens))
