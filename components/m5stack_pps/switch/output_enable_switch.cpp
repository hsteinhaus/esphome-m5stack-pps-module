#include "output_enable_switch.h"

namespace esphome {
namespace m5stack_pps {

void OutputEnableSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_output_enable(state);
}

}  // namespace m5stack_pps
}  // namespace esphome