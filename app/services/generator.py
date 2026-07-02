from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import os
from app.services.validation import validate

def config_type(config):
    if config.device_type == "router":
        return "router_config.j2"
    if config.device_type == "switch":
        return "switch_config.j2"
    
def generate_template(config,template_dir="app/templates"):
    validation = validate(config)
    if validation["status"] == "success":
        try:
            template_name = config_type(config) 
            if not os.path.isdir(template_dir):
                raise FileNotFoundError(f"Template directory '{template_dir}' not found.")
            env = Environment(loader=FileSystemLoader(template_dir))
            template = env.get_template(template_name)
            renderd_config = template.render(**config.model_dump())

            return {
                "status" : "success",
                "config" : renderd_config
            }
            

        except TemplateNotFound:
            return f"Error: Template '{template_name}' not found in '{template_dir}'."
        except Exception as e:
            return f"Error rendering template: {e}"
    
    return validation