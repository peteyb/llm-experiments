'use client';

import { useState } from "react";
import { sendChatMessageChatSendPost } from "../../src/client/sdk.gen";

export default function Chat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSend = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);
    try {
      const res = await sendChatMessageChatSendPost({
        body: { message },
      });
      setResponse(res.data?.response || null);
    } catch (err: any) {
      setError(err.message || "Unknown error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginTop: 32, padding: 16, border: "1px solid #ccc", borderRadius: 8, maxWidth: 800 }}>
      <h3>Simple Chat</h3>
      <input
        type="text"
        value={message}
        onChange={e => setMessage(e.target.value)}
        placeholder="Type your message..."
        style={{ width: "70%", marginRight: 8 }}
        disabled={loading}
      />
      <button onClick={handleSend} disabled={loading || !message.trim()}>
        {loading ? "Sending..." : "Send"}
      </button>
      {error && <div style={{ color: "red", marginTop: 8 }}>Error: {error}</div>}
      {response && <div style={{ marginTop: 8 }}>Response:<br />{response}</div>}
    </div>
  );
} 