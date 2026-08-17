# Plan para el primer commit

## Verificación de identidad

Ejecutar:

```powershell
git config user.name
git config user.email
```

Si alguno no corresponde a tu identidad de GitHub, configurarlo solo para este repositorio:

```powershell
git config --local user.name "Tu nombre"
git config --local user.email "tu-email-verificado-o-noreply-de-github"
```

## Revisar y crear el commit

```powershell
git status
git diff --cached
git add .
git diff --cached
git commit -m "chore: crear estructura inicial del proyecto"
```

No se debe publicar hasta haber revisado que los archivos de datos brutos estén excluidos y que el autor mostrado por Git sea correcto:

```powershell
git show --no-patch --format=fuller HEAD
```

Agregar el remoto y hacer `push` únicamente cuando se decida publicar el repositorio.

