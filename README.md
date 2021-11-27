# wtslog
> Way Too Simple LOGger

This is a small package that literally just exports one class, the `Logger`,
that does one thing: Collect and / or print messages
potentially with indentation.

Originally made because I wanted something simple for
[my adventofcode solutions](https://github.com/kiriDevs/adventofcode),
then made into it's own package because I was tired of importing it like this:

```py
with open("../../_common/logger.py", "w") as logger_module:
    exec(logger_module.read())
LOGGER: Logger = Logger(OUTPUT_PATH)
```
