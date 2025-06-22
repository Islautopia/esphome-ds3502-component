#pragma once
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/output/float_output.h"

namespace esphome {
namespace ds3502 {

class DS3502Output : public output::FloatOutput, public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void write_state(float state) override;
};

}  // namespace ds3502
}  // namespace esphome
