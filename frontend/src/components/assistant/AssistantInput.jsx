import { useState } from "react";
import Button from "../common/Button";

export default function AssistantInput({
  onSend,
  loading,
}) {
  const [text, setText] = useState("");

  const handleSend = () => {
    if (!text.trim()) return;

    onSend(text);
    setText("");
  };

  return (
    <div className="border-t border-slate-200 p-4">

      <textarea
        rows={4}
        value={text}
        placeholder={`Try asking...

• I met Dr. Smith yesterday around 8 PM.
• Change the meeting time to 7 PM.
• Remove brochure.
• Summarize this interaction.
• Give medical insights.
• Recommend next steps.
• Show all meetings with Dr. Smith.`}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            e.stopPropagation();
            handleSend();
          }
        }}
        className="
          w-full
          rounded-xl
          border
          border-slate-300
          bg-slate-50
          p-4
          text-sm
          text-slate-800
          placeholder:text-slate-400
          resize-none
          outline-none
          shadow-sm
          transition-all
          duration-200
          focus:bg-white
          focus:border-blue-600
          focus:ring-4
          focus:ring-blue-100
        "
      />

      <div className="mt-4 flex justify-end">

        <Button
          type="button"
          disabled={loading}
          onClick={handleSend}
          className="
            bg-linear-to-r
            from-blue-600
            to-blue-700
            hover:from-blue-700
            hover:to-blue-800
            text-white
            border-0
            shadow-md
            hover:shadow-lg
            transition-all
            duration-200
          "
        >
          {loading ? "Processing..." : "Send"}
        </Button>

      </div>

    </div>
  );
}