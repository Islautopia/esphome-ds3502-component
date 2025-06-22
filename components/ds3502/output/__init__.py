import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_ID, CONF_OUTPUT_ID
from .. import DS3502Hub # Importamos la clase Hub del __init__.py padre

# Renombramos la clase C++ para evitar conflictos
DS3502Output = cg.esphome_ns.namespace("ds3502").class_(
    "DS3502Output", output.FloatOutput, cg.Component
)
CONF_DS3502_ID = "ds3502_id"

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(DS3502Output),
        cv.Required(CONF_DS3502_ID): cv.use_id(DS3502Hub),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_DS3502_ID])
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)
    cg.add(var.set_hub(hub)) # Llama a la función set_hub en el C++
