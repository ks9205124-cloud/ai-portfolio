import React, { useState } from "react";
import NavBar from "../components/common/navBar";
import "./styles/chat.css";

const API_BASE_URL = process.env.REACT_APP_API_URL || import.meta.env?.VITE_API_URL || "https://ai-portfolio-bwst.onrender.com";

const Chat = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [suggestedQuestions, setSuggestedQuestions] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendMessage = async (userText) => {
        if (!userText.trim()) return;

        setMessages((prev) => [...prev, { role: "user", text: userText }]);
        setInput("");
        setLoading(true);

        try {
            const response = await fetch(`${API_BASE_URL}/chat/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userText }),
            });

            if (!response.ok) {
                throw new Error(`Server responded with ${response.status}`);
            }

            const data = await response.json();

            setMessages((prev) => [
                ...prev,
                { role: "assistant", text: data.response },
            ]);

            fetchSuggestedQuestions();
        } catch (error) {
            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    text: "Something went wrong reaching the chatbot. Please try again.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    };

    const fetchSuggestedQuestions = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/chat/`);
            const data = await response.json();
            setSuggestedQuestions(data.questions || []);
        } catch (error) {
            setSuggestedQuestions([]);
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        sendMessage(input);
    };

    return (
        <React.Fragment>
            <NavBar active="chat" />
            <div className="chat-page">
                <h1>Chat with my resume</h1>

                <div className="chat-messages">
                    {messages.map((msg, idx) => (
                        <div key={idx} className={`chat-bubble ${msg.role}`}>
                            {msg.text}
                        </div>
                    ))}
                    {loading && <div className="chat-bubble assistant">Thinking...</div>}
                </div>

                {suggestedQuestions.length > 0 && (
                    <div className="suggested-questions">
                        {suggestedQuestions.map((q, idx) => (
                            <button key={idx} onClick={() => sendMessage(q)}>
                                {q}
                            </button>
                        ))}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="chat-input-form">
                    <input
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="Ask me anything about my background..."
                    />
                    <button type="submit" disabled={loading}>
                        Send
                    </button>
                </form>
            </div>
        </React.Fragment>
    );
};

export default Chat;