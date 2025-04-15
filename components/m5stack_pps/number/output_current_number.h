#pragma once

#include "esphome/core/component.h"
#include "esphome/components/number/number.h"
#include "../m5stack_pps.h"


namespace esphome {
namespace m5stack_pps {


class M5StackPPSComponent;

class OutputCurrentNumber : public number::Number, public Parented<M5StackPPSComponent> {
  public:
    OutputCurrentNumber() = default;

  protected:
    void control(float value) override;

};

}
}