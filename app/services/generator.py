from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import os
from app.services.validation import validate

def generate_template(config,template_name,template_dir="app/templates"):
    validation = validate(config)
    if validation["status"] == "success":
        try:
            if not os.path.isdir(template_dir):
                raise FileNotFoundError(f"Template directory '{template_dir}' not found.")
            
            env = Environment(loader=FileSystemLoader(template_dir))
            template = env.get_template(template_name)
            return {
                "status" : "success",
                "generated_config" : template.render(**config.dict())
            }

        except TemplateNotFound:
            return f"Error: Template '{template_name}' not found in '{template_dir}'."
        except Exception as e:
            return f"Error rendering template: {e}"
    
    return validation