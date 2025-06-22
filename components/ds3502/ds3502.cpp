#include "ds3502.h"
#include "esphome/core/log.h"

namespace esphome {
namespace ds3502 {

static const char *const TAG = "ds3502";

// --- Implementación del Hub ---
void DS3502Hub::setup() {
  ESP_LOGCONFIG(TAG, "Setting up DS3502 Hub...");
  this->dump_config();
}

void DS3502Hub::dump_config() {
  LOG_I2C_DEVICE(this);
  if (this->is_failed()) {
    LOG_ERROR(TAG, "Communication with DS3502 Hub failed!");
  }
}

void DS3502Hub::set_wiper(uint8_t value) {
  if (this->write(&value, 1) != i2c::ERROR_OK) {
    ESP_LOGE(TAG, "Failed to write to DS3502");
    return;
  }
  ESP_LOGD(TAG, "Hub set wiper to %d", value);
}

// --- Implementación del Output ---
void DS3502Output::write_state(float state) {
  uint8_t wiper_value = static_cast<uint8_t>(state * 127.0f);
  this->hub_->set_wiper(wiper_value);
}

}  // namespace ds3502
}  // namespace esphome
