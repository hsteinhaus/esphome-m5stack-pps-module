import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c, sensor, web_server
from esphome.const import (
    CONF_ID,
    CONF_MODE,
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

from . import CONF_M5STACK_PPS_ID, M5STACK_PPS_COMPONENT_SCHEMA


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

CONFIG_SCHEMA = M5STACK_PPS_COMPONENT_SCHEMA.extend(
        {cv.Optional(type): schema for type, schema in TYPES.items()}
    ).extend(web_server.WEBSERVER_SORTING_SCHEMA)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_M5STACK_PPS_ID])

    for type, _ in TYPES.items():
        if type in config:
            conf = config[type]
            sens = await sensor.new_sensor(conf)
            cg.add(getattr(parent, f"set_{type}_sensor")(sens))