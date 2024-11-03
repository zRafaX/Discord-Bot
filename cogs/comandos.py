from discord.ext import commands

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teste")
    async def ping(self, ctx):
        """Responde com 'teste' para verificar se o bot está ativo."""
        await ctx.send("Teste!")

    @commands.command(name="diga")
    async def diga(self, ctx, *, mensagem: str):
        """O bot repete a mensagem fornecida."""
        await ctx.send(mensagem)

# Configuração da cog
def setup(bot):
    bot.add_cog(Comandos(bot))
