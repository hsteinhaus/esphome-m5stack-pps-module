#pragma once
#include "esphome/core/defines.h"
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

#ifdef USE_SENSOR
#include "esphome/components/sensor/sensor.h"
#endif
#ifdef USE_NUMBER
#include "esphome/components/number/number.h"
#endif
#ifdef USE_SWITCH
#include "esphome/components/switch/switch.h"
#endif
#include "M5ModulePPS.h"


namespace esphome {
namespace m5stack_pps {

class M5StackPPSComponent : public PollingComponent,
                            public i2c::I2CDevice {
#ifdef USE_SENSOR
    SUB_SENSOR(mode)
    SUB_SENSOR(voltage)
    SUB_SENSOR(current)
    SUB_SENSOR(power)
#endif

#ifdef USE_NUMBER
    SUB_NUMBER(output_voltage)
    SUB_NUMBER(output_current)
#endif

#ifdef USE_SWITCH
    SUB_SWITCH(output_enable)
#endif

public:
    void setup() override;
    void dump_config() override;
    float get_setup_priority() const override;
    void update() override;

    void set_output_current(float current);
    void set_output_voltage(float current);
    void set_output_enable(bool enabled);

  private:
    M5ModulePPS pps_{this};
};

}  // namespace m5stack_pps
}  // namespace esphome