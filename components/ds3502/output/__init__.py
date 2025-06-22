import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output, i2c
from esphome.const import CONF_ID

# Declaramos que nuestro componente depende del componente I2C.
DEPENDENCIES = ["i2c"]

ds3502_ns = cg.esphome_ns.namespace("ds3502")
DS3502Output = ds3502_ns.class_("DS3502Output", output.FloatOutput, cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_ID): cv.declare_id(DS3502Output),
    }
).extend(i2c.i2c_device_schema(0x28)).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)
    await i2c.register_i2c_device(var, config)
