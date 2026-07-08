import Button from "../common/Button";

export default function AssistantInput() {
  return (
    <div className="border-t border-slate-200 pt-4">

      <div className="flex gap-3">

        <input
          type="text"
          placeholder="Describe interaction..."
          className="
            flex-1
            rounded-md
            border
            border-slate-300
            px-3
            py-2
            text-sm
            outline-none
            focus:border-blue-500
          "
        />

        <Button>
          Log
        </Button>

      </div>

    </div>
  );
}