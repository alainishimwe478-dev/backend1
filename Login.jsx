import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { login } from "../utils/auth";
import { Mail, Lock, Eye, EyeOff } from "lucide-react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (!email || !password) {
      setError("All fields are required");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const res = await fetch("http://localhost:8000/users/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.detail);

      localStorage.setItem("token", data.token);
      localStorage.setItem("user", JSON.stringify(data.user));

      if (data.user.role === "admin") {
        navigate("/admin-dashboard");
      } else {
        navigate("/user-dashboard");
      }
    } catch (error) {
      setError(error.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[#f3f3f3]">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="w-[340px] rounded-[28px] overflow-hidden shadow-2xl bg-white"
      >
        {/* TOP BLACK SECTION */}
        <div className="bg-black text-white p-8 relative">
          <h2 className="text-2xl font-semibold">Login</h2>
          <p className="text-white/70 text-sm">
            Best way to manage your finances
          </p>

          {/* Decorative lines */}
          <div className="absolute inset-0 opacity-20 pointer-events-none">
            <svg width="100%" height="100%">
              <path d="M0 100 Q150 0 300 100" stroke="white" fill="none" />
              <path d="M0 140 Q150 40 300 140" stroke="white" fill="none" />
            </svg>
          </div>
        </div>

        {/* FORM SECTION */}
        <div className="p-6 space-y-4">
          {/* EMAIL */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <Mail size={18} className="text-gray-400 mr-3" />
            <input
              type="email"
              placeholder="example@gmail.com"
              className="bg-transparent outline-none w-full text-sm"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
                setError("");
              }}
            />
          </div>

          {/* PASSWORD */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <Lock size={18} className="text-gray-400 mr-3" />
            <input
              type={showPassword ? "text" : "password"}
              placeholder="Password"
              className="bg-transparent outline-none w-full text-sm"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
                setError("");
              }}
            />
            <button
              onClick={() => setShowPassword(!showPassword)}
              type="button"
            >
              {showPassword ? (
                <EyeOff size={18} className="text-gray-400" />
              ) : (
                <Eye size={18} className="text-gray-400" />
              )}
            </button>
          </div>

          <div className="text-right">
            <span className="text-xs text-blue-500 cursor-pointer">
              Forget password?
            </span>
          </div>

          {error && <p className="text-red-500 text-xs text-center">{error}</p>}

          {/* LOGIN BUTTON */}
          <button
            onClick={handleLogin}
            disabled={loading}
            className="w-full bg-black text-white py-3 rounded-full font-semibold hover:bg-gray-900 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Logging in..." : "Login"}
          </button>

          {/* SIGNUP */}
          <p className="text-center text-xs text-gray-500 mt-4">
            New user?{" "}
            <span
              onClick={() => navigate("/signup")}
              className="text-blue-500 cursor-pointer"
            >
              Signup
            </span>
          </p>
        </div>
      </motion.div>
    </div>
  );
}
