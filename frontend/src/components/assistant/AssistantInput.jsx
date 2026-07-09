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

            handleSend();

          }

        }}
        className="w-full rounded-lg border border-slate-300 p-3 text-sm resize-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none"
      />

      <div className="mt-3 flex justify-end">

        <Button
          disabled={loading}
          onClick={handleSend}
          bg-gradient-to-r
from-blue-600
to-blue-700
hover:from-blue-700
hover:to-blue-800
shadow-md
hover:shadow-lg
        >
          {loading ? "Processing..." : "Send"}
        </Button>

      </div>

    </div>

  );

}