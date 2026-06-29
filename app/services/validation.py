from app import constants

def validate(config):
        errors= []
        if config.hostname.strip() == "":
                errors.append("hostname is blank")
        elif len(config.hostname) < 4:
                errors.append("invalid hostname - must be at least 4 characters")
        
        if config.device_type not in constants.SUPPORTED_DEVICE_TYPES:
                errors.append("device type is not supported")
        if config.vendor not in constants.SUPPORTED_VENDORS:
                errors.append("vendor is not supported")
        if config.location not in constants.SUPPORTED_LOCATIONS:
                errors.append("invalid location")

        if errors:
                return {"status": "error", "errors": errors}
        return {"status": "success"}