#include "output_voltage_number.h"
#include "esphome/core/log.h"
#include "esphome/core/helpers.h"

namespace esphome {
namespace m5stack_pps {

static const char *const TAG = "m5stack_pps.output";

void OutputVoltageNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_output_voltage(value);
}
}  // namespace m5stack_pps
}  // namespace esphome