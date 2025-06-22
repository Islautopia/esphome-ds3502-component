#include "ds3502.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ds3502 {

static const char *const TAG = "ds3502.output";

void DS3502Output::setup() {
  ESP_LOGCONFIG(TAG, "Setting up DS3502 Output component from GitHub...");
  this->dump_config();
}

void DS3502Output::dump_config() {
  LOG_OUTPUT(this);
  LOG_I2C_DEVICE(this);
  if (this->is_failed()) {
    LOG_ERROR(TAG, "Communication with DS3502 failed!");
  }
}

void DS3502Output::write_state(float state) {
  uint8_t wiper_value = static_cast<uint8_t>(state * 127.0f);
  if (this->write(&wiper_value, 1) != i2c::ERROR_OK) {
    ESP_LOGE(TAG, "Failed to write to DS3502");
    return;
  }
  ESP_LOGD(TAG, "Setting wiper to %d (state: %.2f)", wiper_value, state);
}

}  // namespace ds3502
}  // namespace esphome
