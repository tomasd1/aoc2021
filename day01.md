# day01

## input

```elixir
values = File.read!("data01.txt")
|> String.split("\n") |> Enum.map(&String.to_integer(&1))
```

## solution A

```elixir
accumulate = &Enum.reduce(&1, %{last: nil, count: 0}, fn item, acc ->
    count = if item > acc.last, do: acc.count + 1, else: acc.count
    %{last: item, count: count}
  end)

values |> accumulate.() |> Map.get(:count)
```

## solution B

```elixir
Enum.chunk_every(values, 3, 1, :discard)
|> Enum.map(&Enum.sum(&1)) |> accumulate.() |> Map.get(:count)
```
