#pragma once

#include "esphome/components/sensor/sensor.h"
#include "../m5stack_pps.h"

namespace esphome {
namespace m5stack_pps {

enum SensorChannel {
    SENSOR_MODE,
    SENSOR_VOLTAGE,
    SENSOR_CURRENT,
    SENSOR_POWER,
};

class InputSensor : public Component, public sensor::Sensor, public Parented<M5StackPPSComponent> {
 public:
    InputSensor() = default;
    void set_channel(SensorChannel sc) { this->sensor_channel_ = sc; }
protected:
    SensorChannel sensor_channel_;
};

}  // namespace m5stack_pps
}  // namespace esphome