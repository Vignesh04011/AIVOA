export default function Select({
  label,
  options = [],
}) {
  return (
    <div className="flex flex-col gap-2">
      <label className="text-sm font-medium text-slate-700">
        {label}
      </label>

      <select
        className="
          h-10
          w-full
          rounded-md
          border
          border-slate-300
          bg-white
          px-3
          text-sm
          outline-none
          transition
          focus:border-blue-500
          focus:ring-2
          focus:ring-blue-200
        "
      >
        {options.map((option) => (
          <option key={option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
}