from importlib import import_module
from config.utils import ImproperlyConfigured


def get_config_var(var_name, config_module):
    """Get specified variable from config module

    Args:
        var_name (str): The name of the variable to access from the config
        module object.
        config_module (object): the config module
            from which you access variable settings.

    Raises:
        valueError: If `var_name` isn't in
            the `config_module` object.

    Returns:
        str: The value of `var_name` in the `config_module` object.
    """
    try:
        return config_module.__dict__[var_name]
    except (AttributeError, KeyError):
        import config.base as cb
        try:
            return cb.__dict__[var_name]
        except:
            err_msg = "Couldn't find {} in base config module, " \
                      "are you sure that's the variable name?".format(var_name)
            raise ImproperlyConfigured(err_msg)

def process_config_file(request):
    """Process and load valid configs from command line arg --config

    Args:
        request (object): conftest object to introspect test environment

    Raises:
        ImportError: Raise if module specified via command arg --config does
            not exist
    """
    config_name = request.config.getoption('--config')
    try:
        user_config = import_module(config_name)
        return user_config
    except ImportError:
        error_msg = 'No config named {}. Make sure you\'re correctly ' \
                    'referencing where config is saved'.format(config_name)
        raise ImportError(error_msg)

    except AttributeError:
        err_msg = 'Specify a config to use or remove the config flag'
        raise ImportError(err_msg)