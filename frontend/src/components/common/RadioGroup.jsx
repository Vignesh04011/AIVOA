export default function RadioGroup() {
  return (
    <div className="flex gap-6">

      <label className="flex items-center gap-2 text-sm">
        <input type="radio" name="sentiment" />
        Positive
      </label>

      <label className="flex items-center gap-2 text-sm">
        <input type="radio" name="sentiment" />
        Neutral
      </label>

      <label className="flex items-center gap-2 text-sm">
        <input type="radio" name="sentiment" />
        Negative
      </label>

    </div>
  );
}