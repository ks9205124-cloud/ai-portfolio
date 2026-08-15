const INFO = {
	main: {
		title: "portfolio",
		name: "Shaurya Shukla",
		email: "shawshuk007@gmail.com",
		logo: "../logo.png",
	},

	socials: {
		twitter: "https://twitter.com/",
		github: "https://github.com/ks9205124-cloud",
		linkedin: "https://linkedin.com/",
		instagram: "https://instagram.com/",
		stackoverflow: "https://stackoverflow.com/",
		facebook: "https://facebook.com/",
	},

	homepage: {
		title: "Backend software engineer, AI engineering enthusiast, and Big-O whisperer.",
		description:
			"I'm a second-year CS student focused on backend development with Java and Spring Boot. I build things end-to-end — from a hand-written parser that analyzes code complexity, to a full OAuth2 authorization server, to an AI chatbot that answers questions about this very resume. I like understanding systems deeply rather than reaching for the easy shortcut, and I'm always looking for the next hard problem to work through.",
	},

	about: {
		title: "I'm Shaurya. I'm a second-year CS student building real systems, not just following tutorials.",
		description:
			"I'm currently focused on backend engineering with Java and Spring Boot, while self-studying AI engineering (LLM APIs, prompt engineering, structured outputs) as a second track. My projects reflect a preference for depth over shortcuts — building a real AST-based parser instead of a heuristic, self-hosting OAuth2 instead of reaching for an external auth provider. My goal is a software engineering internship, and I'm always open to feedback, collaboration, or a good technical conversation.",
	},

	articles: {
		title: "Notes on backend engineering, AI systems, and the occasional deep dive into how things actually work.",
		description:
			"Thoughts on the projects I've built, design decisions I've made, and things I've learned the hard way.",
	},

	projects: [
		{
			title: "Time Complexity Analyzer",
			description:
				"Analyzes source code and determines its Big O time complexity using a hand-written lexer and recursive-descent parser — builds a real AST and walks it to compute complexity, including detecting logarithmic patterns in loops. Spring Boot + MySQL backend, deployed live on Render.",
			logo: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg",
			linkText: "View Project",
			link: "https://github.com/ks9205124-cloud/time-complexity-analyzer",
		},

		{
			title: "Expense Tracker",
			description:
				"Full-stack expense tracker with a self-hosted OAuth2 implementation — built as both an authorization server and resource server following Spring Security in Action, rather than using an external provider. Full Authorization Code + PKCE flow, Spring Boot backend, React frontend, containerized with Docker Compose.",
			logo: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg",
			linkText: "View Project",
			link: "https://github.com/ks9205124-cloud/expenseTracker",
		},

		{
			title: "Sudoku Solver",
			description:
				"A vanilla Java/Swing desktop app that solves Sudoku puzzles of dynamic n×n size — not fixed to the standard 9x9 grid. Uses a solve-first, then-hide-cells approach to generate puzzles.",
			logo: "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/java/java.png",
			linkText: "View Project",
			link: "https://github.com/ks9205124-cloud/sudokuApp",
		},

		{
			title: "AI Portfolio Chatbot",
			description:
				"The chatbot powering this very site — built in Python with the Groq API, structured and schema-validated responses via Pydantic, and conversation history management. Ask it anything about my background.",
			logo: "https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python.png",
			linkText: "View Project",
			link: "https://github.com/ks9205124-cloud/ai-portfolio",
		},
	],
};

export default INFO;