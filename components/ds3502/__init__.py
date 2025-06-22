import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output, i2c
from esphome.const import CONF_ID

# 1. Declaramos la dependencia, como sabemos que es necesario.
DEPENDENCIES = ["i2c"]

# 2. Definimos el namespace y la clase C++ que vamos a usar.
ds3502_ns = cg.esphome_ns.namespace("ds3502")
DS3502Output = ds3502_ns.class_("DS3502Output", output.FloatOutput, cg.Component, i2c.I2CDevice)

# 3. Definimos el CONFIG_SCHEMA para la plataforma 'ds3502' dentro del componente 'output'.
#    ESPHome sabe que este schema es para la plataforma 'output' porque hereda de output.FLOAT_OUTPUT_SCHEMA.
CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_ID): cv.declare_id(DS3502Output),
    }
).extend(i2c.i2c_device_schema(0x28)).extend(cv.COMPONENT_SCHEMA)

# 4. Definimos la función para generar el código C++.
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)
    await i2c.register_i2c_device(var, config)
