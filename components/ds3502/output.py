import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_ID
from . import DS3502Hub # Importamos el Hub desde __init__.py

CONF_DS3502_ID = "ds3502_id"

DS3502Output = cg.esphome_ns.namespace("ds3502").class_("DS3502Output", output.FloatOutput, cg.Component)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(DS3502Output),
    cv.Required(CONF_DS3502_ID): cv.use_id(DS3502Hub),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_DS3502_ID])
    var = cg.new_Pvariable(config[CONF_ID], hub)
    await cg.register_component(var, config)
    await output.register_output(var, config)
