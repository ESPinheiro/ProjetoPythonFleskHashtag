from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from comunidadeImpresionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
    confirmacao_senha = PasswordField('Confirmação da Senha',validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro E-mail ou faça login para continuar')

class FormLogin(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de Acesso')
    botao_submit_login = SubmitField('Fazer login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuario',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil',validators=[FileAllowed(['jpg','png'])])

    curso_Execel = BooleanField('Execel')
    curso_Python = BooleanField('Python ')
    curso_PowerBI = BooleanField('PowerBI')
    curso_VBA = BooleanField('VBA')
    curso_SQL = BooleanField('SQL')
    curso_CSharp = BooleanField('C#')
    curso_HTML = BooleanField('HTML')
    curso_CSS = BooleanField('CSS')
    curso_JavaScript = BooleanField('JavaScript')
    curso_Java = BooleanField('Java')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self,email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado no sistema. Cadastre outro e-mail')

class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired() ,Length(2,140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
