#pragma once

#include "esphome/components/switch/switch.h"
#include "../m5stack_pps.h"

namespace esphome {
namespace m5stack_pps {

class OutputEnableSwitch : public switch_::Switch, public Parented<M5StackPPSComponent> {
 public:
 OutputEnableSwitch() = default;

 protected:
  void write_state(bool state) override;
};

}  // namespace m5stack_pps
}  // namespace esphome