#include "output_number.h"
#include "esphome/core/log.h"
#include "esphome/core/helpers.h"

namespace esphome {
namespace m5stack_pps {

static const char *const TAG = "m5stack_pps.output";

void OutputNumber::control(float value) {
  this->publish_state(value);
  switch (this->output_channel_) {
    case OUTPUT_VOLTAGE:
      this->parent_->set_output_voltage(value);
      break;
    case OUTPUT_CURRENT:
      this->parent_->set_output_current(value);
      break;
  }
}
}  // namespace m5stack_pps
}  // namespace esphome