#pragma once
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/output/float_output.h"

namespace esphome {
namespace ds3502 {

// Clase para el "Hub" I2C
class DS3502Hub : public Component, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void set_wiper(uint8_t value);
};

// Clase para el "Output" que usa el Hub
class DS3502Output : public output::FloatOutput, public Component {
 public:
  DS3502Output(DS3502Hub *hub) : hub_(hub) {}
  void write_state(float state) override;

 protected:
  DS3502Hub *hub_;
};

}  // namespace ds3502
}  // namespace esphome
