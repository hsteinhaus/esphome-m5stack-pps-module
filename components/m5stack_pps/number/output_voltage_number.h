#pragma once

#include "esphome/core/component.h"
#include "esphome/components/number/number.h"
#include "../m5stack_pps.h"


namespace esphome {
namespace m5stack_pps {


class M5StackPPSComponent;

class OutputVoltageNumber : public number::Number, public Parented<M5StackPPSComponent> {
  public:
    OutputVoltageNumber() = default;

  protected:
    void control(float value) override;
};

}
}