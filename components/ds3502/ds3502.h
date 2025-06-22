#pragma once
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace ds3502 {

class DS3502Hub : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void set_wiper(uint8_t value);
};

}  // namespace ds3502
}  // namespace esphome
