values = File.read!("data01.txt")
|> String.split("\n") |> Enum.map(&String.to_integer(&1))

accumulate = &Enum.reduce(&1, %{last: nil, count: 0}, fn item, acc ->
  count = if item > acc.last, do: acc.count + 1, else: acc.count
  %{last: item, count: count}
end)

# Part A
values |> accumulate.() |> Map.get(:count) |> IO.puts()

# Part B
Enum.chunk_every(values, 3, 1, :discard)
|> Enum.map(&Enum.sum(&1)) |> accumulate.() |> Map.get(:count) |> IO.puts()
