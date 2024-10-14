from flask import render_template, url_for, redirect, flash
from app import app, db
from app.forms import CompanyInformationForm
from app.models import CompanyInformation

@app.route('/')
@app.route('/index', endpoint='index')
@app.route('/se')
def se():
    lang = "sv"
    companyInformationId = 1
    companyInformation = CompanyInformation.query.get(companyInformationId)
    return render_template('index.html', lang=lang, companyInformation=companyInformation)

# To implement:
# 1. Check that the phone number is formatted correctly
@app.route('/admin', methods=['GET', 'POST'], endpoint='admin')
def admin():
    form = CompanyInformationForm()
    companyInformationId = 1
    companyInformation = CompanyInformation.query.get(companyInformationId)
    lang = "sv"

    if form.validate_on_submit():
        companyInformation.companyPhoneNumber = form.phoneNumber.data
        db.session.commit()
        flash('Phone number updated to: {}'.format(companyInformation.companyPhoneNumber))
        return redirect(url_for('admin'))

    #Pre poulate form input
    form.phoneNumber.data = companyInformation.companyPhoneNumber

    return render_template('admin.html', lang=lang, form=form)