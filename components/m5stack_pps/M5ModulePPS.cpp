#include "M5ModulePPS.h"
#include "esphome/core/log.h"

bool M5ModulePPS::writeBytes(uint8_t addr, uint8_t reg, uint8_t *buffer,
                             uint8_t length)
{
    ESP_LOGD("pps", "writing addr 0x%02x,  reg 0x%02x, len: %d", addr, reg, length);
    return _i2c_dev->write_bytes(reg, buffer, length);
}

bool M5ModulePPS::readBytes(uint8_t addr, uint8_t reg, uint8_t *buffer, uint8_t length) {
    ESP_LOGD("pps", "reading addr 0x%02x,  reg 0x%02x, len: %d", addr, reg, length);
    return _i2c_dev->read_bytes(reg, buffer, length);
}

void M5ModulePPS::float_to_bytes(float s, uint8_t *d) {
    union {
        float value;
        uint8_t bytes[4];
    } f2b;
    f2b.value = s;
    memcpy(d, f2b.bytes, 4);
}

float M5ModulePPS::bytes_to_float(uint8_t *s) {
    union {
        float value;
        uint8_t bytes[4];
    } f2b;
    memcpy(f2b.bytes, s, 4);
    return f2b.value;
}

uint16_t M5ModulePPS::getID(void) {
    uint8_t wbuf[1] = {MODULE_ID_L};
    uint8_t rbuf[2] = {0};
    readBytes(_addr, MODULE_ID_L, rbuf, 2);
    return (rbuf[1] << 8 | rbuf[0]);
}

void M5ModulePPS::setPowerEnable(bool en) {
    uint8_t wbuf[1] = {0};
    wbuf[0] = en ? 0x01 : 0;
    writeBytes(_addr, MODULE_ENABLE, wbuf, 1);
}

uint8_t M5ModulePPS::getPowerEnable(void) {
    uint8_t rbuf[1] = {0};
    readBytes(_addr, MODULE_ENABLE, rbuf, 1);
    return rbuf[0];
}

uint8_t M5ModulePPS::getMode(void) {
    uint8_t rbuf[1];
    readBytes(_addr, PSU_RUNNING_MODE, rbuf, 1);
    return rbuf[0];
}

float M5ModulePPS::getVIN(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_VIN_READBACK_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

float M5ModulePPS::getTemperature(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_TEMP_READBACK_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

float M5ModulePPS::getReadbackVoltage(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_VOUT_READBACK_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

void M5ModulePPS::setOutputVoltage(float vol) {
    uint8_t wbuf[4] = {0};
    float_to_bytes(vol, wbuf);
    writeBytes(_addr, PSU_VOUT_SET_1, wbuf, 4);
}

float M5ModulePPS::getOutputVoltage(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_VOUT_SET_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

float M5ModulePPS::getReadbackCurrent(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_IOUT_READBACK_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

void M5ModulePPS::setOutputCurrent(float cur) {
    uint8_t wbuf[4] = {0};
    float_to_bytes(cur, wbuf);
    writeBytes(_addr, PSU_IOUT_SET_1, wbuf, 4);
}

float M5ModulePPS::getOutputCurrent(void) {
    uint8_t rbuf[4] = {0};
    readBytes(_addr, PSU_IOUT_SET_1, rbuf, 4);
    return bytes_to_float(rbuf);
}

void M5ModulePPS::getUID(uint32_t *uid0, uint32_t *uid1, uint32_t *uid2) {
    uint8_t rbuf[12] = {0};

    readBytes(MODULE_POWER_ADDR, PSU_PSU_ID_W0, rbuf, 12);

    *uid0 = (rbuf[0] | (rbuf[1] << 8) | (rbuf[2] << 16) | (rbuf[3] << 24));
    *uid1 = (rbuf[4] | (rbuf[5] << 8) | (rbuf[6] << 16) | (rbuf[7] << 24));
    *uid2 = (rbuf[8] | (rbuf[9] << 8) | (rbuf[10] << 16) | (rbuf[11] << 24));
}
