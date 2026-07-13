export default function RadioGroup({
  value,
  onChange,
}) {

  const sentiments = [
    "Positive",
    "Neutral",
    "Negative",
  ];

  return (
    <div className="flex gap-6">

      {sentiments.map((item) => (

        <label
          key={item}
          className="flex items-center gap-2 text-sm"
        >

          <input
            type="radio"
            name="sentiment"
            value={item}
            checked={
              value?.trim().toLowerCase() ===
              item.toLowerCase()
            }
            onChange={(e) => onChange(e.target.value)}
          />

          {item}

        </label>

      ))}

    </div>
  );
}