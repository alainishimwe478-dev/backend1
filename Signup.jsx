import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { signup } from "../utils/auth";
import { Mail, Lock, User, Phone, Eye, EyeOff } from "lucide-react";

export default function Signup() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    password: "",
  });

  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
    setError("");
  };

  const handleSignup = async () => {
    if (!form.name || !form.email || !form.phone || !form.password) {
      setError("All fields are required");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const user = await signup(
        form.name,
        form.email,
        form.phone,
        form.password,
      );
      alert("Signup successful 🎉");
      navigate("/login");
    } catch (error) {
      setError(error.message || "Signup failed");
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
        {/* TOP BLACK HEADER */}
        <div className="bg-black text-white p-8 relative">
          <h2 className="text-2xl font-semibold">Signup</h2>
          <p className="text-white/70 text-sm">
            Best way to manage your finances
          </p>

          {/* Decorative curves */}
          <div className="absolute inset-0 opacity-20 pointer-events-none">
            <svg width="100%" height="100%">
              <path d="M0 100 Q150 0 300 100" stroke="white" fill="none" />
              <path d="M0 140 Q150 40 300 140" stroke="white" fill="none" />
            </svg>
          </div>
        </div>

        {/* FORM */}
        <div className="p-6 space-y-4">
          {/* NAME */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <User size={18} className="text-gray-400 mr-3" />
            <input
              name="name"
              placeholder="Jenny Wilson"
              className="bg-transparent outline-none w-full text-sm"
              value={form.name}
              onChange={handleChange}
            />
          </div>

          {/* EMAIL */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <Mail size={18} className="text-gray-400 mr-3" />
            <input
              name="email"
              placeholder="example@gmail.com"
              className="bg-transparent outline-none w-full text-sm"
              value={form.email}
              onChange={handleChange}
            />
          </div>

          {/* PHONE */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <Phone size={18} className="text-gray-400 mr-3" />
            <input
              name="phone"
              placeholder="123-456-789"
              className="bg-transparent outline-none w-full text-sm"
              value={form.phone}
              onChange={handleChange}
            />
          </div>

          {/* PASSWORD */}
          <div className="flex items-center bg-gray-100 rounded-full px-4 py-3">
            <Lock size={18} className="text-gray-400 mr-3" />
            <input
              type={showPassword ? "text" : "password"}
              name="password"
              placeholder="Password"
              className="bg-transparent outline-none w-full text-sm"
              value={form.password}
              onChange={handleChange}
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
            >
              {showPassword ? (
                <EyeOff size={18} className="text-gray-400" />
              ) : (
                <Eye size={18} className="text-gray-400" />
              )}
            </button>
          </div>

          {error && <p className="text-red-500 text-xs text-center">{error}</p>}

          {/* SIGNUP BUTTON */}
          <button
            onClick={handleSignup}
            disabled={loading}
            className="w-full bg-black text-white py-3 rounded-full font-semibold hover:bg-gray-900 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Creating Account..." : "Signup"}
          </button>

          {/* LOGIN LINK */}
          <p className="text-center text-xs text-gray-500 mt-4">
            Already have an account?{" "}
            <span
              onClick={() => navigate("/login")}
              className="text-blue-500 cursor-pointer"
            >
              Login
            </span>
          </p>
        </div>
      </motion.div>
    </div>
  );
}
