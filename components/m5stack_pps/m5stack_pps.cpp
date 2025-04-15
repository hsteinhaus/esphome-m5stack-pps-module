#include "m5stack_pps.h"

#include "esphome/core/log.h"

namespace esphome {
namespace m5stack_pps {

static const char *TAG = "m5stack_pps.sensor";

float M5StackPPSComponent::get_setup_priority() const {
    return setup_priority::DATA;
}

void M5StackPPSComponent::setup() {
    ESP_LOGCONFIG(TAG, "M5STACKPPS: setup");
    uint16_t id = pps_.getID();
    ESP_LOGI(TAG, "PPS ID: 0x%04x", id);

    uint32_t uid[3];
    pps_.getUID(uid, uid+1, uid+2);
    ESP_LOGD(TAG, "PPS UID : %08x:%08x:%08x", uid[0], uid[1], uid[2]);

    if (output_voltage_number_ != nullptr) {
        output_voltage_number_->publish_state(0.5);
    }
    if (output_current_number_ != nullptr) {
        output_current_number_->publish_state(0.0);
    }
    if (output_enable_switch_ != nullptr) {
        output_enable_switch_->publish_state(false);
    }
}

void M5StackPPSComponent::update() {
    uint8_t mode = pps_.getMode();
    float current = pps_.getReadbackCurrent();
    float voltage = pps_.getReadbackVoltage();
    float power = current * voltage;

    if (this->mode_sensor_ != nullptr) {
        this->mode_sensor_->publish_state(mode);
    }

    if (this->voltage_sensor_ != nullptr) {
        this->voltage_sensor_->publish_state(voltage);
    }

    if (this->current_sensor_ != nullptr) {
        this->current_sensor_->publish_state(current);
    }

    if (this->power_sensor_ != nullptr) {
        this->power_sensor_->publish_state(power);
    }
}

void M5StackPPSComponent::dump_config() {
    ESP_LOGCONFIG(TAG, "M5STACKPPS:");
    LOG_I2C_DEVICE(this);

    if (this->is_failed()) {
        ESP_LOGE(TAG, "Communication with M5Stack PPS Module failed!");
        return;
    }
    LOG_UPDATE_INTERVAL(this);
    LOG_SENSOR("  ", "Voltage", this->voltage_sensor_);
    LOG_SENSOR("  ", "Current", this->current_sensor_);
    LOG_SENSOR("  ", "Power", this->power_sensor_);
}


void M5StackPPSComponent::set_output_current(float current) {
    ESP_LOGI(TAG, "setting output current to %f A", current);
    pps_.setOutputCurrent(current);
}

void M5StackPPSComponent::set_output_voltage(float voltage) {
    ESP_LOGI(TAG, "setting output voltage to %f V", voltage);
    pps_.setOutputVoltage(voltage);
}

void M5StackPPSComponent::set_output_enable(bool enabled) {
    ESP_LOGI(TAG, "setting output enable to %d", enabled);
    pps_.setPowerEnable(enabled);
}


}  // namespace m5stack_pps
}  // namespace esphome