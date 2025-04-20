#pragma once

#include "esphome/core/component.h"
#include "esphome/components/number/number.h"
#include "../m5stack_pps.h"


namespace esphome {
namespace m5stack_pps {

enum OutputChannel {
  OUTPUT_VOLTAGE,
  OUTPUT_CURRENT,
};

class M5StackPPSComponent;

class OutputNumber : public Component, public number::Number, public Parented<M5StackPPSComponent> {
  public:
    OutputNumber(const OutputChannel oc) { this->output_channel_ = oc; }
  protected:
    void control(float value) override;
    OutputChannel output_channel_;
};

}
}