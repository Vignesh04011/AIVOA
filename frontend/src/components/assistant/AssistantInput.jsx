import { useState } from "react";
import Button from "../common/Button";

export default function AssistantInput({
  onAutoFill,
}) {

  const [text, setText] = useState("");

  return (

    <div className="border-t border-slate-200 pt-4">

      <textarea
        rows={5}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Describe your interaction with the HCP..."
        className="w-full rounded-md border p-3 text-sm"
      />

      <Button
  className="mt-3 bg-blue-600 text-white border-blue-600 hover:bg-blue-700"
  onClick={() => {
      onAutoFill(text);
      setText("");
  }}
>
    Send
</Button>

    </div>

  );

}