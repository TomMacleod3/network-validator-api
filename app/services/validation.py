def validate(config):
        errors= []
        if config.hostname.strip() == "":
                errors.append("hostname is blank")
        elif len(config.hostname) < 4:
                errors.append("invalid hostname - must be at least 4 characters")
        
        if config.device_type not in {"router", "switch", "firewall"}:
                errors.append("device type is not supported")

        if errors:
                return {"status": "error", "errors": errors}
        return {"status": "success"}