**Basic usage:**

```python
import time

from lubar import ProgressBar

total = 100
bar = ProgressBar(total)
for i in bar(range(total)):
    time.sleep(0.05)
```

**Keyword Arguments:**

* `size`: size of the progress bar (default to `37`)

* `description`: progress description (default to `''`)

* `file`: file object to print progress bar to it (default to `sys.stdout`)

* `progressed_char`: progress character (default to `'#'`)

* `remained_char`: remain character (default to `'.'`)

* `enclosing_chars`: characters to enclose progress bar between them (default to `('[', ']')`)

* `join_char`: character to join progress bar parts (default to `'  '`)

*Note: All attributes can be updated at run time. I designed this progress bar to train deep learning models in PyTorch. I needed a progress bar to update it description in training loops to print model's losses values.*

*Special credit to [eusoubrasileiro](https://stackoverflow.com/users/1207193/eusoubrasileiro). I designed this progress based on his answer in [Stack Overflow](https://stackoverflow.com/a/34482761/12412938)*