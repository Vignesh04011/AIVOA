import Input from "../common/Input";

export default function DiscussionSection() {
  return (
    <div className="mt-6 space-y-5">
      <Input
        label="Attendees"
        placeholder="Enter names or search..."
      />

      <div>
        <label className="mb-2 block text-sm font-medium text-slate-700">
          Topics Discussed
        </label>

        <textarea
          rows={5}
          placeholder="Enter key discussion points..."
          className="
            w-full
            rounded-lg
            border
            border-slate-300
            bg-white
            p-3
            text-sm
            outline-none
            transition
            focus:border-blue-500
            focus:ring-2
            focus:ring-blue-200
            resize-none
          "
        />
      </div>

      <button
        className="
          rounded-lg
          border
          border-slate-300
          bg-white
          px-4
          py-2
          text-sm
          font-medium
          hover:bg-slate-50
        "
      >
        🎤 Summarize from Voice Note
      </button>
    </div>
  );
}