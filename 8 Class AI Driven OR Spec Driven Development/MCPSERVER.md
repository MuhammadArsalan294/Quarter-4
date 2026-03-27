Class 8(Part D)

Book Referece:

https://ai-native.panaversity.org/

Book on click
Part 2: AI Tool Landscape on click
Chapter 5: How It All Started __ The Claude Code.. on click
MCP Integration: Connecting to External Systems on click

# 1) Playwright MCP (browse the web)
claude mcp add --transport stdio playwright npx @playwright/mcp@latest

# 2) Context7 MCP (get up-to-date docs)
claude mcp add --transport stdio context7 npx @upstash/context7-mcp

--------------------------------

Hackathon 1 on click
mcp server on click
cmd 
claude mcp list (asey check krein gay ky mcp server conect hai ya nh)

claude mcp add --transport stdio context7 npx @upstash/context7-mcp (agar connect nhi hai tw ye command run kar do)

--------------------------------
Second MCP Server Connected:
.claude.json (Yani window ky command prompt mein code . likh kar vs code open karna hai waha ye file mile gi)


"github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}" 
    }
}
(Ye  .claude.json main paste karni hai   "env": {} es ky nechy. Ye github official mcp server sy lia hai code)

https://github.com/MuhammadArsalan294 (apni repo main aye then setting on click then developer setting on click then personal access token on click then Fine-grained tokens on click then Generate new token on click. Token name * claude-mcp and generate token on click and copy token )


"github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer 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" #(Yaha token paste karna hai )
    }
}
(token paste kar dia)


claude mcp list (Ye upper terminal py ja kar check karna hai ky mcp server github ka connect hua ya nhi )
ccr code (Ye terminal py run karni hai or claude open ho jaye ga)
/mcp list (Ye claude ky search bar mein ja kar bhi check karna hai ky mcp server connected hai ya nhi)




