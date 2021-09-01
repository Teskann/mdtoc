# mdtoc Examples

## Example 1

In this example, we generate a table of contents at the
[specified place](./before.md#L7) with the default settings.

```commandline
mdtoc before.md
```

>:heavy_check_mark: [before](before.md) :arrow_right: [after](after_2.md)

## Example 2

In this example, we generate a table of contents at the
[specified place](./before.md#L7). We generate a level 2 title for the
table of contents, and we ignore the level 1 titles (the main title).

```commandline
mdtoc before.md -m 2 -l 2
```

>:heavy_check_mark: [before](before.md) :arrow_right: [after](after_1.md)

## Example 3

In this example, we generate a table of contents at the
[specified place](./before.md#L7). We generate a level 2 title for the
table of contents. We change this title to *ToC*. For a better readability,
we ignore the titles with level > 3.

```commandline
mdtoc before.md -M 3 -l 2 -t ToC
```

>:heavy_check_mark: [before](before.md) :arrow_right: [after](after_3.md)